import gradio as gr

def parse_input(array_str: str):
    """
    Convert a comma-separated string like '5, 3, 8, 1'
    into a Python list of integers.
    """
    array_str = array_str.strip()
    if not array_str:
        raise ValueError("Input cannot be empty. Please enter numbers like: 5, 3, 8, 1")

    parts = array_str.split(",")
    nums = []
    for p in parts:
        p = p.strip()
        if p == "":
            continue
        try:
            nums.append(int(p))
        except ValueError:
            raise ValueError(
                f"'{p}' is not a valid integer. Use only integers separated by commas, e.g. 10, 4, 7."
            )
    if len(nums) == 0:
        raise ValueError("No valid numbers found. Please enter at least one integer.")
    return nums


def bubble_sort_with_steps(array_str: str):
    """
    Runs Bubble Sort and returns:
    - A sorted list (string)
    - A step-by-step explanation (string)
    """
    try:
        arr = parse_input(array_str)
    except ValueError as e:
        return f"Error: {e}", ""

    steps = []
    n = len(arr)
    steps.append(f"Initial list: {arr}")

    for i in range(n):
        swapped = False
        steps.append(f"\nPass {i + 1}:")
        for j in range(0, n - i - 1):
            steps.append(f"  Compare {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                steps.append(f"    Swap → {arr[j+1]} moves left")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                steps.append(f"    List is now: {arr}")
            else:
                steps.append(f"    No swap → list stays: {arr}")
        if not swapped:
            steps.append("  No swaps this pass → list is sorted early.")
            break
        else:
            steps.append(f"End of pass {i + 1}: {arr}")

    steps.append(f"\nFinal sorted list: {arr}")
    sorted_list_str = ", ".join(str(x) for x in arr)
    steps_text = "\n".join(steps)

    return sorted_list_str, steps_text


with gr.Blocks() as demo:
    gr.Markdown(
        """
    # Bubble Sort Visualizer 🫧

    Enter a list of integers separated by commas (example: `5, 3, 8, 1`).

    This app will:
    - Parse your input
    - Run **Bubble Sort**
    - Show the **final sorted list**
    - Show a **step-by-step explanation** of each comparison and swap
    """
    )

    input_box = gr.Textbox(
        label="Enter numbers (comma-separated)",
        placeholder="Example: 5, 3, 8, 1, 2",
        lines=1,
    )

    sort_button = gr.Button("Run Bubble Sort")

    sorted_output = gr.Textbox(label="Sorted result", interactive=False)
    steps_output = gr.Textbox(
        label="Step-by-step explanation",
        lines=20,
        interactive=False,
    )

    sort_button.click(
        fn=bubble_sort_with_steps,
        inputs=input_box,
        outputs=[sorted_output, steps_output],
    )

if __name__ == "__main__":
    demo.launch()
