import TodoItem from "./TodoItem";
import styles from "./todolist.module.css";

interface Props {
    todos: string[];
}

export default function TodoList({ todos }: Props) {
    return (
        <div className={styles.list}>
            {todos.map((item) => (
                <TodoItem key={item} item={item} />
            ))}
        </div>
    );
}
