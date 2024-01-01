import HeaderSep from "./HeaderSep";

export default function HeaderLinks() {
    return (
        <div className="float-left inline-block font-bold ml-4">
            <a className="text-blue-500" href="#">
                Updates
            </a>
            <HeaderSep />
            <a className="text-blue-500" href="#">
                Support
            </a>
            <HeaderSep />
            <a className="text-blue-500" href="#">
                Logout
            </a>
        </div>
    );
}
