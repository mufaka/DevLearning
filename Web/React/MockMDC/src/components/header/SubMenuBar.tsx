import { useLocation } from "react-router-dom";

const pageTitles: { [id: string]: string } = {
    "/": "Practice Manager Home",
    "/perform": "Performance",
    "/appts": "Appointments",
};

export default function SubMenuBar() {
    const location = useLocation();

    return (
        <div className="h-6 w-screen">
            <div className="float-left">Time and Date</div>
            <div className="float-right">{pageTitles[location.pathname]}</div>
        </div>
    );
}
