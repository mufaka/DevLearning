/*
Utility functions for handling DOM load. This file is meant to be reusable and will call
a pages "__dom_init" function if it is defined.

Additionally, there are some utility methods meant for reducing redundant code. JQuery does
this and a lot more but opting for a lighter weight alternative that only has utilities needed
for this project.
*/
document.addEventListener('DOMContentLoaded', function() {
    if (__dom_init) {
        __dom_init();
    }
});

/*
Gets an element by it's css selector
*/
function getElement(selector) {
    return document.querySelector(selector);
}