from sqlmodel import Session, select


#cargar registros en la db
def send_data_to_db(pos, data):
    print(data)
    
    conn = connection_db()
    cur = conn.cursor()
    sql = '''
    INSERT INTO clients
    (nombre_cliente, direccion_cliente, telefono_cliente,correo_electronico_cliente, fecha_cumpleanos)
    VALUES (%s, %s, %s, %s, %s);
    '''
    print(data)
    values = (data["Nombre_Cliente"][pos], data["Dirección_Cliente"][pos], data["Teléfono_Cliente "][pos], data["Correo_Electrónico_Cliente"][pos], data["Fecha_Cumpleaños"][pos])
    
    cur.execute(sql,values)
    conn.commit()
    conn.close()
    
    return {"Message": "Data inserted"}

#crear cliente
def create_reg():
    
    conn = connection_db()
    
    cursor = conn.cursor()
    
    sql_create = '''
    INSERT INTO clients
    (nombre_cliente, direccion_cliente, telefono_cliente,correo_electronico_cliente, fecha_cumpleanos)
    VALUES (%s, %s, %s, %s, %s);
    '''
        
    values=('Roger', 'carrer el que sigui', '678113452', 'correu@correu.com', '12_09_1999')

    cursor.execute(sql_create,values)
    
    conn.commit()
    
    conn.close()
    cursor.close()
    
#obtener todos los clientes
def read_reg():
    conn = connection_db()
    cursor = conn.cursor()
    
    sql_read = "SELECT * FROM clients"
    
    cursor.execute(sql_read)
    conn.commit()
    
    results = cursor.fetchall()
    
    return results
#obtener cliente por id
def read_reg_by_id(id):
    conn = connection_db()
    cur = conn.cursor()
    sql = '''
    SELECT * 
    FROM clients 
    WHERE id_cliente = %s
    '''
    values = (id,)
    cur.execute(sql,values)
    conn.commit()
    results = cur.fetchall()
    return results

#actualizar cliente
def update_reg(telefono,nombre,id):
    conn = connection_db()
    cursor =  conn.cursor()
    sql_update = '''
            UPDATE clients 
            SET telefono_cliente =  %s, nombre_cliente = %s
            WHERE id_cliente = %s
            '''
    values = (telefono, nombre,id)
    cursor.execute(sql_update,values)
    conn.commit()
    conn.close()
    
    return{"Update successfully"}

#eliminar cliente
def delete_reg(id):
    conn = connection_db()
    cursor = conn.cursor()
    sql = '''
    DELETE FROM clients
    WHERE id_cliente= %s
    '''
    values = (id,)
    cursor.execute(sql,values)
    conn.commit()
    conn.close()
    cursor.close()
    return{"Delete successfully"}
    