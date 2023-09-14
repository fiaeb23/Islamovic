import streamlit as st
import hashlib, csv, time

if "user" not in st.session_state:
    st.session_state["user"] = None

st.write(st.session_state)

def get_hash(pw: str):
    pw = pw.encode()
    return hashlib.sha256(pw).hexdigest()

def login(user_name: str, hashed_user_pw: str) -> str:
    with open(r"data\user_db.csv", encoding="utf-8") as file:
        for name, pw in list(csv.reader(file))[1:]:
            if name == user_name and pw == hashed_user_pw:
                return name

def register(user_name: str, hashed_user_pw: str) -> bool:
    # check if user already exists:
    with open(r"data\user_db.csv", encoding="utf-8") as file:
        for name, pw in list(csv.reader(file))[1:]:
            if name == user_name:
                return False
    
    # write new user
    with open(r"data\user_db.csv", "a", encoding="utf-8", newline="") as file:
        csv.writer(file).writerow([user_name, hashed_user_pw])
        return True

st.title("👻 App")

if st.session_state["user"] is None:
    tab_login, tab_register, tab_admin = st.tabs(["Login", "Register", "Admin"])

    with tab_login:
        with st.form("login"):
            in_user_name = st.text_input("Nutzername:")
            in_user_pw = st.text_input("Passwort:", type="password") 
            
            if st.form_submit_button("Login"):
                user = login(in_user_name, get_hash(in_user_pw))
                if user:
                    st.session_state["user"] = user
                    st.write("Erfolgreich eingeloggt!")
                else:
                    st.write("Das hat nicht geklappt!")
                
                time.sleep(1)
                st.experimental_rerun()
    
    with tab_register:
        with st.form("register", clear_on_submit=True):
            in_user_name = st.text_input("Nutzername:")
            in_user_pw_1 = st.text_input("Passwort:")
            in_user_pw_2 = st.text_input("Passwort (Zum Bestätigen):")
            if st.form_submit_button("Register"):
                if in_user_pw_1 != in_user_pw_2:
                    st.write("Passwörter sind nicht gleich!")                 
                elif len(in_user_pw_1) < 3:
                    st.write("Passwort zu kurz!")
                else:
                    register_successful = register(in_user_name, get_hash(in_user_pw_1))
                    if not register_successful:
                        st.write(f"Nutzer {in_user_name} existiert bereits!")
                    else:
                        st.write("Erfolgreich neuen Nutzer angelegt!")
                    
                time.sleep(2)                
                st.experimental_rerun()

    with tab_admin:
        if st.button("Reload User DB"):
            with open(r"data\user_db.csv", "w", newline="") as file:
                csv_w = csv.writer(file)
                csv_w.writerow(["user_name","user_pw"])
                csv_w.writerow(["admin","a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"])
                csv_w.writerow(["esad","b3a8e0e1f9ab1bfe3a36f231f676f78bb30a519d2b21e6c530c0eee8ebb4a5d0xyz"])
                

else:
    st.header(f'Hallo {st.session_state["user"]}')
    if st.button("Logout"):
        st.session_state["user"] = None
        st.experimental_rerun()