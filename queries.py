#drop tables

vehicle_class_drop = 'drop table if exists vehicle_class'
vehicle_drop = 'drop table if exists vehicle'


# create tables
 
vehicle_class_create = '''create table if not exists vehicle_class(
            class char(3),
            name text,
            primary key (class))'''

vehicle_create = '''create table if not exists vehicle(
            vehicle_id char(6),
            name text,
            price float,
            capacity int,
            speed float,
            accel float,
            brake float,
            handl float,
            class char(3),
            primary key (vehicle_id),
            foreign key (class) references vehicle_class)'''


# insert tables

vehicle_class_insert = '''insert into vehicle_class(
            class, name ) values (?,?)'''
            
vehicle_insert = ''' insert into vehicle(vehicle_id, name, price, capacity, speed, accel, brake, handl, class)
            values(?,?,?,?,?,?,?,?,?)'''


# query lists

create_table_queries = [vehicle_class_create, vehicle_create]
drop_table_queries = [vehicle_class_drop, vehicle_drop]


