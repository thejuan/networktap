 urlsnarf | awk -F' ' '{printf("insert into urls (machine, url) values( '\''%s'\'','\''%s'\'');\n", $1,  $7)}' | sqlite3 /opt/monitor/log.db

