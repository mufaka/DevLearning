//import { useState } from "react";
import "./App.css";
import Hello from "./components/Hello";
import Message from "./components/Message";
import DemoForm from "./components/DemoForm";

function App() {
    // NOTE: The initial load time for this is slow; I think it is the typescript compilation and thus probably only
    //       a dev related issue. Refreshing the page after the initial load is quick.

    // NOTE: from what I understand, this is bad because changes to this state will cause a re-render of the entire
    //       DOM. React doesn't know if children (and their children) need this state so it naively re-renders recursively.
    // const [count, setCount] = useState(0);

    // NOTE: This entire thing could have been done in about 2 minutes but trying
    //       to stay optimistic on the overall advantage here.

    // NOTE: Initial thoughts are that this really isn't a good way to build large web applications that have different
    //       layouts and a ton of UI elements ... but Facebook, so work off the assumption that there is a benefit long term.
    //       Perhaps not seeing the forest through the tree right now ...
    //          this should help: https://maxrozen.com/examples-of-large-production-grade-open-source-react-apps

    // You can pass an object in as props
    const person1 = {
        id: 1,
        name: "Bill",
        age: 51,
    };

    const person2 = {
        id: 2,
        name: "Michelle",
        age: 47,
    };

    // NOTE: The empty <></> tags are required to group the output because a React component
    //       can only return 1 element.
    return (
        <>
            {/* This is how you comment inside of a React component */}
            {/* Pass an array of objects to the component as Props */}
            <Hello people={[person1, person2]} />
            <Message />
            <Message />
            <DemoForm />
        </>
    );
}

export default App;
