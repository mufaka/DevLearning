import { useNavigate } from "react-router-dom";

import {
    HomeOutlined,
    DashboardOutlined,
    CalendarOutlined,
    BookOutlined,
    HistoryOutlined,
    DollarOutlined,
    BarsOutlined,
    BankOutlined,
    ContainerOutlined,
    AuditOutlined,
    PrinterOutlined,
    BarChartOutlined,
    MailOutlined,
    PushpinOutlined,
    LaptopOutlined,
    SettingOutlined,
} from "@ant-design/icons";

const menuItemClass =
    "float-left mt-1 ml-1.5 border-gray-800 border-r-4 pr-1.5 text-gray-400 hover:text-blue-400 cursor-pointer";

const menuItemSelectedClass =
    "float-left mt-1 ml-1.5 border-gray-800 border-r-4 pr-1.5 text-blue-300 hover:text-blue-400";

const iconStyle = { fontSize: "20px" };
const iconClassName = "pt-1";
const badgeStyle = "block";

export default function MenuBar() {
    const navigate = useNavigate();
    return (
        <div className="h-14 w-screen bg-gray-700">
            <div
                className={menuItemSelectedClass}
                onClick={() => navigate("/")}
            >
                <HomeOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Home</span>
            </div>
            <div className={menuItemClass} onClick={() => navigate("/perform")}>
                <DashboardOutlined
                    className={iconClassName}
                    style={iconStyle}
                />
                <span className={badgeStyle}>Perform</span>
            </div>
            <div className={menuItemClass} onClick={() => navigate("/appts")}>
                <CalendarOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Appts</span>
            </div>
            <div className={menuItemClass}>
                <BookOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Charts</span>
            </div>
            <div className={menuItemClass}>
                <HistoryOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>History</span>
            </div>
            <div className={menuItemClass}>
                <DollarOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Invoice</span>
            </div>
            <div className={menuItemClass}>
                <BarsOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>eSlips</span>
            </div>
            <div className={menuItemClass}>
                <BankOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Pay</span>
            </div>
            <div className={menuItemClass}>
                <ContainerOutlined
                    className={iconClassName}
                    style={iconStyle}
                />
                <span className={badgeStyle}>Claims</span>
            </div>
            <div className={menuItemClass}>
                <AuditOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Post</span>
            </div>
            <div className={menuItemClass}>
                <PrinterOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Stmts</span>
            </div>
            <div className={menuItemClass}>
                <BarChartOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Reports</span>
            </div>
            <div className={menuItemClass}>
                <MailOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Msgs</span>
            </div>
            <div className={menuItemClass}>
                <PushpinOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Remind</span>
            </div>
            <div className={menuItemClass}>
                <LaptopOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Portal</span>
            </div>
            <div className={menuItemClass}>
                <SettingOutlined className={iconClassName} style={iconStyle} />
                <span className={badgeStyle}>Setting</span>
            </div>
        </div>
    );
}
