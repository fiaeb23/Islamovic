import streamlit as st
import hashlib
import sqlite3

def create_connection():
    path = r"C:\Users\lbeikzadeh\Desktop\my_project\projekt.db"
    with sqlite3.connect(path) as conn:
        return conn.cursor()

def get_hash(pw: str):
    pw = pw.encode()
    return hashlib.sha256(pw).hexdigest()
if "menu" not in st.session_state:    
    st.session_state["menu"]="login"

if  st.session_state["menu"]=="login" :
     
    tab1, tab2= st.tabs(["Einloggen 1", "Registrieren 2"])

    with tab1:
        with st.form("log_form",clear_on_submit=True):
            st.write("Bitte einlogen")
            i_name=st.text_input("name" ,placeholder = "name")
            i_password = st.text_input("password" ,type = "password")
            i_password = get_hash(i_password)
        
            if st.form_submit_button("Bestätigen"):
                sql = "SELECT * FROM register_user WHERE username=? AND password=?;"
                cursor = create_connection()
                cursor.execute(sql,(i_name,i_password,))
                result = cursor.fetchall()
                if result :
                    st.session_state["menu"]="main"
                    st.success("Erfolgreich eingeloggt!")
                    st.experimental_rerun()
                    
    with tab2:
        with st.form("reg_form",clear_on_submit=True):
            st.write("Bitte einlogen")
            i_name=st.text_input("name" ,placeholder = "name")
            i_password = st.text_input("password" ,type = "password",key="1")
            #i_password = get_hash(i_password)
            i_password2 = st.text_input("password" ,type = "password", key="2")
            
            if st.form_submit_button("Bestätigen"):
                
                if i_password == i_password2:
                    cursor = create_connection()
                    st.write("❤")
                    sql = "SELECT * FROM register_user WHERE username=?"
                    cursor.execute(sql,(i_name,))
                    result = cursor.fetchall()
                    if not result:
                        cursor = create_connection()
                        sql = "INSERT INTO register_user (username,password) VALUES (?,?)"
                        i_password = get_hash(i_password)
                        cursor.execute(sql,[i_name,i_password,])
                        cursor.connection.commit()
                        sql="SELECT * FROM register_user"
                        cursor.execute(sql)
                        result=cursor.fetchall()
                        st.table(result)
                        #st.experimental_rerun()
                        
elif st.session_state["menu"]=="main" :
        st.write("willkommen")
        
        if st.button ("auslogen") :
            st.session_state["menu"]="login"
            st.experimental_rerun()
        
   
   

