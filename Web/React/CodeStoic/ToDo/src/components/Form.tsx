import { useState } from "react";
import styles from "./form.module.css";

interface Props {
    todos: string[];
    setTodos: (values: any) => void; // pass a function in props
}

export default function Form({ todos, setTodos }: Props) {
    const [todo, setTodo] = useState("");

    function handleSubmit(e: React.FormEvent<HTMLElement>) {
        // dont post the form
        e.preventDefault();

        // use the spread operator to add to the array
        setTodos([...todos, todo]);

        // clear the current todo value, this will clear the input field
        setTodo("");
    }

    return (
        <form className={styles.todoform} onSubmit={handleSubmit}>
            <div className={styles.inputContainer}>
                <input
                    className={styles.modernInput}
                    type="text"
                    value={todo}
                    onChange={(e) => setTodo(e.currentTarget.value)}
                    placeholder="Enter Todo Item..."
                />
                <button className={styles.modernButton} type="submit">
                    Add
                </button>
            </div>
        </form>
    );
}
