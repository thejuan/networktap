 urlsnarf | awk -F' ' '{printf("insert into urls (machine, occurred, url) values( '\''%s'\'','\''%s'\'','\''%s'\'');\n", $1, substr($4,2), $7)}' | sqlite3 /opt/monitor/log.db

