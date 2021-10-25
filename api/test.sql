drop table if exists entries;
create table user (
  id integer primary key autoincrement,
  created_at timestamp not null default current_timestamp,

  username string not null,
  email string not null ,
  password string not null
);