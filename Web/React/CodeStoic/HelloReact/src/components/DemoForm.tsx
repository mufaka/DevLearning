import { useState } from "react";

// forms in react are ugggh.
// The code stoic videos aren't using TypeScript so this is more of
// learning curve than just watching those.

export default function DemoForm() {
    // For a complex form this state object should probably be somewhere else?
    // Also, we probably would want to load initial state and that would be better
    // served by some type of view data.
    const [form, setFormValue] = useState({ firstName: "", lastName: "" });

    function handleSubmit(e: React.MouseEvent<HTMLElement>) {
        e.preventDefault();
        console.log(form);

        // TODO: Validation? Data driven forms? Much more needs to be covered here but
        //       this is where the lesson stopped.
    }

    return (
        <form>
            <input
                onChange={(e) => {
                    return setFormValue({
                        ...form,
                        firstName: e.currentTarget.value,
                    });
                }}
                type="text"
                value={form.firstName}
            />
            <input
                onChange={(e) => {
                    return setFormValue({
                        ...form,
                        lastName: e.currentTarget.value,
                    });
                }}
                type="text"
                value={form.lastName}
            />
            <button onClick={(e) => handleSubmit(e)}>Add</button>
        </form>
    );
}
