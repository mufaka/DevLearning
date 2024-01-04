import { useLocation } from "react-router-dom";

const pageTitles: { [id: string]: string } = {
    "/": "Practice Manager Homepage",
    "/perform": "Performance",
    "/appts": "Appointments",
};

export default function SubMenuBar() {
    const location = useLocation();

    let options: Intl.DateTimeFormatOptions = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
    };
    let today = new Date();

    return (
        <div className="h-6 w-screen bg-white text-gray-800 text-base border-b-2 border-black">
            <div className="float-left text-blue-600 font-semibold ml-1">
                {today.toLocaleDateString("en-US", options)}
            </div>
            <div className="float-right font-extrabold mr-1">
                {pageTitles[location.pathname]}
            </div>
        </div>
    );
}
