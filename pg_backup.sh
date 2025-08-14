#!/bin/bash

PASSPHRASE=""
# Location to place backups.
backup_dir="backups/clusters"
#String to append to the name of the backup files
backup_date=`date +%d-%m-%Y`
#Numbers of days you want to keep copie of your databases
number_of_days=15
for cluster in 10.229.0.12
#for cluster in 10.229.0.12 10.229.0.2 10.229.0.6 10.229.0.21
    do
    mkdir -p $backup_dir/$cluster
    databases=`psql -l -t -h $cluster -U sa | cut -d'|' -f1 | sed -e 's/ //g' -e '/^$/d'`
    for i in $databases; do  if [ "$i" != "postgres" ] && [ "$i" != "template0" ] && [ "$i" != "template1" ] && [ "$i" != "cloudsqladmin" ]; then
        echo Dumping $i from $cluster to $backup_dir/$cluster/$i\_$backup_date.sql
        pg_dump --format=plain --no-owner --no-acl -h $cluster -U sa $i | sed -E 's/(DROP|CREATE|COMMENT ON) EXTENSION/-- \1 EXTENSION/g' > $backup_dir/$cluster/$i\_$backup_date.sql
        # pg_dump $i > $backup_dir$i\_$backup_date.sql
        # bzip2 $backup_dir$cluster\_$i\_$backup_date.sql
        tar -zOc $backup_dir/$cluster/$i\_$backup_date.sql | gpg -c --batch --passphrase $PASSPHRASE -o $backup_dir/$cluster/$i\_$backup_date.sql.tar.gz.gpg
	rm $backup_dir/$cluster/$i\_$backup_date.sql
      fi
    done
done
