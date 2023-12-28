import { useState } from "react";

export default function Message() {
    // define state for this component
    // NOTE: setCount is a function name but we don't define a function with that name ... we can just call it.
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }

    return (
        <div>
            <button onClick={handleClick}>
                You have clicked me {count} times!
            </button>
        </div>
    );
}
