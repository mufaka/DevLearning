// import { useState } from "react";
// import "./App.css";
import PageLayout from "./pages/PageLayout";
import { BrowserRouter, Routes, Route } from "react-router-dom";

// TODO: There is a way to lazy load these to improve startup performance
import Home from "./pages/Home";
import Perform from "./pages/Perform";
import Appts from "./pages/Appts";

function App() {
    // const [count, setCount] = useState(0);

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<PageLayout />}>
                    <Route index element={<Home />} />
                    <Route path="perform" element={<Perform />} />
                    <Route path="appts" element={<Appts />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
