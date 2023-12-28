// typescript wants a type ... should this be defined somewhere else?
// can a component import other js?
interface Person {
    id: number;
    name: string;
    age: number;
}

interface Props {
    people: Person[];
}

function displayMessage(person: Person) {
    return `Hello, ${person.name}`;
}

// destructure props
// NOTE: props are immutable? Not really if you are destructuring.
//       But, as a rule, you shouldn't modify them .. but what about formatting?
//       Formatting should be OK semantically as the data stays the same.
//       What about conversions? eg: USD $1.00 = X other currency?
function Hello({ people }: Props) {
    return people.map((person: Person) => {
        return <h3 key={person.id}>{displayMessage(person)}</h3>;
    });
}

export default Hello;
