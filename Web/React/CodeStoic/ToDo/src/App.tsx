import Todo from "./components/Todo";
import Header from "./components/Header";
import "./App.css";

function App() {
    return (
        <>
            <Header />
            <Todo />
        </>
    );
}

export default App;

/*
Stopping this tutorial here as the basics of the component layout, props, state, and
event handlers but this intro leaves a lot of questions:

1. This isn't a practical way to build large, complex web apps. 
    a. css modules should have access to shared styles (they may, but not covered)
    b. Every element is potentially a component which makes it very tedious
    c. It's still not clear what the benefit is over vanilla js for updating styles and content
    d. Different page layouts are not covered in this tutorial
    e. All data needs to be API driven which isn't terrible but server side rendering will be faster
    f. Hooks seem to let devs get in trouble with DOM re-rendering which defeats the whole purpose
    g. The SPA size can get unreasonably large affecting load time
    h. How SEO friendly can you make an SPA? Does it even matter if you build an app and have a marketing site as well?

2. It does seem like a fun way to build the front end and there is a huge ecosystem of components that
   should allow for rapid development if there are ones that meet your needs.
    a. stitching together other third party components could be tricky depending on what you choose
    b. if it's your core product, you should own the IP

3. Currently running this with npm run dev
    a. I know that there is some type of bundling that happens for publishing.
        i) What does that entail?
        ii) Find a DevOps guide on deploying React apps.

4. Nothing about this tutorial demonstrates the promise of being able to more rapidly build front ends
    a. The opposite seems true, at least for this simple example. It would be much easier to use vanilla js to get the same functionality.

TODO: I feel like I've just scratched the surface of JSX, especially with TypeScript. Need to do a deeper
dive into those.

NOTE: I'm not in a position where I could comfortably start a project from scratch but know enough to at least
get around an existing code base. So maybe some of the questions / statements above will be answered / refuted 
when I learn more.

NOTE: spider senses are tingling a little bit with the prospect of possibly being able to take a static layout and generate components. HTML represents a DOM
that should be able to be iterated and decisions could be made on what the component structure should be. CSSOM is also a thing that could be used for styling; 
just need a parser or perhaps take advantage of a browser plugin like Grease/Tamper Monkey.

Need to find a real world example tutorial that includes authentication, logging, is data driven, and includes multiple layouts
to decide. Need to also understand best practices for larger implementations as well as accumulate a cheat sheet of anti-patterns
to look out for.

TODO: Compare and contrast this to Angular, Vue, and Blazor. Perhaps come up with a reasonably sized demonstration app and implement
in all 4 (React, Angular, Vue, Blazor) to make an educated decision.
   
*/
