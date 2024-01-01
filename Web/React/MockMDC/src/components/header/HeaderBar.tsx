import Logo from "./Logo";
import UserPractice from "./UserPractice";
import HeaderLinks from "./HeaderLinks";

export default function HeaderBar() {
    return (
        <div className="h-8 w-screen bg-black p-0.5">
            <div className="float-left w-44 my-0.5 mx-1.5">
                <Logo />
            </div>
            <div className="float-right my-0.5 mx-1.5">
                <UserPractice />
                <HeaderLinks />
            </div>
        </div>
    );
}
