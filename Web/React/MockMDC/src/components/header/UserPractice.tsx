import HeaderSep from "./HeaderSep";

export default function UserPractice() {
    return (
        <div className="float-left inline-block text-white font-bold">
            User: Bill Nickel
            <HeaderSep />
            <select className="text-black rounded text-sm p-0.5">
                <option value="0" selected>
                    Demo Practice
                </option>
                <option value="1">Development Practice</option>
                <option value="2">Platinum Survey</option>
            </select>
        </div>
    );
}
