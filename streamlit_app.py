import streamlit as st
import itertools

def find_combinations(numbers, target):
    try:
        number_list = [int(float(i) * 100) for i in numbers.split('\n') if i.strip()]
        target_list = int(target * 100)
        result = [seq for i in range(len(number_list), 0, -1)
                  for seq in itertools.combinations(number_list, i)
                  if sum(seq) == target_list]
        result_list = [tuple(x / 100.0 for x in tpl) for tpl in result]
        return result_list
    except ValueError:
        return None

def main():
    st.title("Find Combinations App")

    st.write("Enter numbers separated by newlines and specify the target value.")

    numbers_input = st.text_area("Enter numbers here (one per line)")
    target_input = st.number_input("Enter the target value", step=0.01)

    if st.button("Find Combinations"):
        if numbers_input.strip() == "":
            st.warning("Please enter numbers.")
        else:
            result_list = find_combinations(numbers_input, target_input)
            if result_list is not None and len(result_list) > 0:
                st.write("Result:")
                st.write(result_list)
            else:
                st.warning("Error: Ensure numbers are properly formatted and target value is achievable.")

if __name__ == "__main__":
    main()

