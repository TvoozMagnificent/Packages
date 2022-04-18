import sqlite3

# functions
def connect_database(database_name=":memory:"):
    return sqlite3.connect(database_name)
connect=connect_database

def create_table(connection, table_name, rownames, types, extra_fields=[]):
    if not extra_fields:
        extra_fields = [""] * len(rownames)
    RETURN, all_data = "\n", zip(rownames, types, extra_fields)
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS {table_name} 
    ({f',{RETURN}'.join([' '.join(data_line) for data_line in all_data])})"""
    )
createT=create_table

def delete_table(connection, table_name):
    connection.execute(
        f"""DROP TABLE IF EXISTS {table_name}"""
    )
deleteT=delete_table

def insert_data(
    connection,
    table_name,
    values_list,
    error_display="!ERROR default",
    show_errors=True,
    edit_if_error=False,
    suppress_warning_empty_error_display=True,
):
    try:
        connection.execute(
            f"INSERT INTO COMPANY \
        VALUES {tuple(values_list)}"
        )
        # In[8]: f'{(1, 2)}'
        # Out[8]: '(1, 2)'
    except Exception as e:
        print(
            show_errors
            * (str(e) if error_display == "!ERROR default" else error_display)
        )
        # True*"a string" = "a string", False*"anything" = ""
        if edit_if_error:
            connection.execute(
                f"REPLACE INTO COMPANY \
            VALUES {tuple(values_list)}"
            )
            # In[8]: f'{(1, 2)}'
            # Out[8]: '(1, 2)
            if not error_display and not suppress_warning_empty_error_display:
                print(
                    "WARNING: You have used insert_data() for replacing a row. "
                    "This is inefficient and you should use the change_data() function. "
                    "To suppress this warning, use suppress_warning_empty_error_display=True"
                )
insertD=insert_data

def insert_datas(
    connection,
    table_name,
    values_lists,
    error_display="!ERROR default",
    show_errors=True,
):
    for values_list in values_lists:
        insert_data(connection, table_name, values_list, error_display, show_errors)
insertDs=insert_datas

def commit_changes(connection):
    connection.commit()
commit=commit_changes

def select_data(
    connection,
    table_name,
    rownames=["*"],
    constraints="1",
    ordering="",
    asc_or_desc="ASC",
    limit="-1",
):
    return [
        list(row)
        for row in connection.execute(
            f"SELECT "
            f"{' AND '.join(rownames)} "
            f"FROM {table_name} "
            f"WHERE {constraints} "
            f"{bool(ordering) * f'ORDER {ordering} {asc_or_desc} LIMIT {limit}'}"
        )
    ]
selectD=select_data

def get_list(connection, table_name):
    return [list(row) for row in connection.execute(f"SELECT * FROM {table_name}")]
getlist=get_list

def change_data(connection, table_name, values):
    connection.execute(
        f"REPLACE INTO COMPANY \
        VALUES {tuple(values)}"
    )
changeD=change_data

def change_datas(connection, table_name, values):
    for value in values:
        change_data(connection, table_name, value)
changeDs=change_datas

def delete_data(
    connection,
    table_name,
    rownames=["*"],
    constraints="1",
    ordering="",
    asc_or_desc="ASC",
    limit="-1",
):
    return [
        list(row)
        for row in connection.execute(
            f"DELETE FROM {table_name} "
            f"WHERE {constraints} "
            f"{bool(ordering) * f'ORDER {ordering} {asc_or_desc} LIMIT {limit}'}"
        )
    ]
deleteD=delete_data

def close_connection(connection):
    connection.close()
close=close_connection

# constants
connection_from_memory = ":memory:"
ascending_order = "ASC"
descending_order = "DESC"
select_all = "*"
no_constraint = "1"
no_limit = "-1"
display_raised_error = "!ERROR default"
RETURN = "\n"


# format func
def format_func(list_,start='-',sep='|',extras=None,suppress_warning_empty_error_display=False):
    if extras==None:
        extras=['']*4
    elif not isinstance(extras,list):
        extras=[extras]*4
    elif len(extras)==0:
        extras=['']*4
    elif len(extras)==1:
        extras=extras*4
    elif len(extras)!=4:
        print(
            f"WARNING: You have used format_func() and put a different value for extras: {extras}. "
            "This is not allowed. "
            "To suppress this warning, use suppress_warning_empty_error_display=True. "
            "Thus, nothing is done. "
        )
        return
    pre = "\n".join(
        [
            f"{sep}  {''.join(z)}"
            for z in [
                [
                    f"{(f'{y},').ljust(13)}{sep} " f" "
                    for y in str(tuple(x))[1:-1].split(", ")
                ]
                for x in list_
            ]
        ]
    )
    extras[0],extras[1],extras[2],extras[3]=str(extras[0]),str(extras[1]),str(extras[2]),str(extras[3])
    var1=(len(pre.split(RETURN)[0])-2)
    part=var1//len(start)*start + start[:var1%len(start)]
    var2,var3=len(extras[0])+len(extras[1]),len(extras[2])+len(extras[3])
    return f"{extras[0]}{part[:len(part)-var2]}{extras[1]}\n{pre}\n{extras[2]}{part[:len(part)-var3]}{extras[3]}"
format_=format_func

def formatted_data(connection,table_name,start='-',sep='|',extras=None,suppress_warning_empty_error_display=False):
    return format_func(get_list(connection,table_name),
                       start=start,
                       extras=extras,
                       sep=sep,
                       suppress_warning_empty_error_display=suppress_warning_empty_error_display)
formatted=formatted_data

def print_data(connection,table_name,start='-',sep='|',extras=None,suppress_warning_empty_error_display=False):
    print(formatted_data(connection,table_name,start,sep,extras,suppress_warning_empty_error_display))
print_=print_data

constants={}

constants["connection_from_memory"] = ":memory:"
constants["ascending_order"] = "ASC"
constants["descending_order"] = "DESC"
constants["select_all"] = "*"
constants["no_constraint"] = "1"
constants["no_limit"] = "-1"
constants["display_raised_error"] = "!ERROR default"
constants["RETURN"] = "\n"

