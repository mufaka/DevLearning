import { useState } from "react";
import TodoList from "./TodoList";
import Form from "./Form";

export default function Todo() {
    // this list will be shared between sub-components through props
    const [todos, setTodos] = useState<string[]>([]);

    return (
        <div>
            {/* you can pass state as props */}
            <Form todos={todos} setTodos={setTodos} />
            <TodoList todos={todos} />
        </div>
    );
}
