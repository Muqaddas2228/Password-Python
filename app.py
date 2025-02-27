import streamlit as st  
import string
import random

# Characters to generate password from
all_characters_pattern = list(string.ascii_letters + string.digits + "!@#$%^&*()")
alphanumeric_pattern = list(string.ascii_letters + string.digits)
common_passwd_pattern = ["password", "computer", "1234"]

# Function to generate a random password
def generate_random_password2(characters: list, password_length=6) -> str:
    random.shuffle(characters)
    password = [random.choice(characters) for _ in range(password_length)]
    return "".join(password)

# NATO Phonetic Alphabet
natophonetics = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
    "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
    "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey",
    "X": "X-Ray", "Y": "Yankee", "Z": "Zulu"
}

# Leet Dictionary
leet_dict = {'a': '4', 'b': 'l3', 'c': '(', 'd': '[)', 'e': '3', 'l': '1', 's': '5', 't': '+', 'w': '\\/\\/', 'o': '0'}

def get_natophonetics(term):
    return ' '.join([natophonetics.get(i, i) for i in list(term.upper())])

def leet_converter(term):
    return ' '.join([leet_dict.get(i, i) for i in list(term.lower())])

def main():
    st.title("🔐 Password Generator App 🔥")
    
    menu = ["🏠 Home", "⚙️ Advanced", "🔢 LeetConverter", "ℹ️ About"]
    choice = st.sidebar.selectbox("📜 Menu", menu)

    if choice == "🏠 Home":
        st.subheader("🏡 Home")
        passwd_pattern_list = ['🔠 Alphanumeric', '🔢 All', '📝 Words']
        password_length = st.number_input("🔢 Password Length", min_value=5, max_value=25, value=8)
        password_pattern_choice = st.multiselect("🎭 Pattern", passwd_pattern_list, default='🔢 All')
        
        if st.button("✨ Generate"):
            st.info("🎉 Generated Results")
            if '🔠 Alphanumeric' in password_pattern_choice:
                passwd_result = generate_random_password2(alphanumeric_pattern, password_length)
                st.code(passwd_result)
                st.info("📢 NATO Phonetics")
                st.write(f"🧠 Remember:: {get_natophonetics(passwd_result)}")

            elif '🔠 Alphanumeric' and '📝 Words' in password_pattern_choice:
                first_result = generate_random_password2(alphanumeric_pattern, password_length)
                passwd_result = str(first_result) + random.choice(common_passwd_pattern)
                st.code(passwd_result)
                st.info("📢 NATO Phonetics")
                st.write(f"🧠 Remember:: {get_natophonetics(passwd_result)}")

            else:
                passwd_result = generate_random_password2(all_characters_pattern, password_length)
                st.code(passwd_result)
                st.info("📢 NATO Phonetics")
                st.write(f"🧠 Remember:: {get_natophonetics(passwd_result)}")

    elif choice == "⚙️ Advanced":
        st.subheader("⚙️ Advanced")
        passwd_pattern_list = ['🔠 Alphanumeric', '🔢 All']
        password_length = st.number_input("🔢 Password Length", min_value=5, max_value=25, value=8)
        custom_word = st.text_input("✍️ Add Your Custom Word")
        password_pattern_choice = st.multiselect("🎭 Pattern", passwd_pattern_list, default='🔢 All')
        
        if st.button("✨ Generate"):
            st.info("🎉 Generated Results")
            first_result = generate_random_password2(all_characters_pattern, password_length)
            passwd_result = random.choice([custom_word]) + str(first_result)
            st.code(passwd_result)
            st.info("📢 NATO Phonetics")
            st.write(f"🧠 Remember:: {get_natophonetics(passwd_result)}")

    elif choice == "🔢 LeetConverter":
        st.subheader("🔢 Leet Converter")
        col1, col2 = st.columns(2)
        
        with col1:
            term = st.text_area("✍️ Your Text")
            if st.button("🔄 Convert"):
                st.success("🎉 Results")
                st.write(leet_converter(term))

    else:
        st.subheader("ℹ️ About")
        st.write("🔐 This is a simple password generator app built with Streamlit! 🚀")

if __name__ == '__main__':
    main()
