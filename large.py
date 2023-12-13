import streamlit as st

def find_largest_number(nums):
    return max(nums)

def main():
    st.title("Find the Largest Number")

    # Sidebar for input
    with st.sidebar:
        st.header("Enter three numbers:")
        numbers = [st.number_input(f"Number {i + 1}", value=0) for i in range(3)]

    # Main content area
    st.write("## Result:")
    
    # Button to find the largest number
    if st.button("Find Largest Number"):
        largest_number = find_largest_number(numbers)

        # Output display in the center
        st.markdown(
            f"<h1 style='text-align: center; color: green;'>The largest number is: {largest_number}</h1>",
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
