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
    "float-left mt-1.5 ml-1.5 border-gray-800 border-l-4 pl-1.5";
const iconStyle = { fontSize: "32px" };
const iconClassName = "text-gray-400 hover:text-blue-400";

export default function MenuBar() {
    return (
        <div className="h-12 w-screen bg-gray-700">
            <div className={menuItemClass}>
                <HomeOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <DashboardOutlined
                    className={iconClassName}
                    style={iconStyle}
                />
            </div>
            <div className={menuItemClass}>
                <CalendarOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <BookOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <HistoryOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <DollarOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <BarsOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <BankOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <ContainerOutlined
                    className={iconClassName}
                    style={iconStyle}
                />
            </div>
            <div className={menuItemClass}>
                <AuditOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <PrinterOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <BarChartOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <MailOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <PushpinOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <LaptopOutlined className={iconClassName} style={iconStyle} />
            </div>
            <div className={menuItemClass}>
                <SettingOutlined className={iconClassName} style={iconStyle} />
            </div>
        </div>
    );
}
