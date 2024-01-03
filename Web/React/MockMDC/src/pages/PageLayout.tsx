import { Layout, Flex } from "antd";
import HeaderBar from "../components/header/HeaderBar";
import MenuBar from "../components/header/MenuBar";
import SubMenuBar from "../components/header/SubMenuBar";
import { Outlet } from "react-router-dom";

const { Header, Footer, Content } = Layout;

const headerStyle: React.CSSProperties = {
    textAlign: "center",
    color: "#fff",
    height: 112,
    padding: 0,
    //paddingInline: 48,
    lineHeight: "unset",
    backgroundColor: "#4096ff",
};

const contentStyle: React.CSSProperties = {
    textAlign: "center",
    minHeight: 120,
    lineHeight: "120px",
    color: "#fff",
    backgroundColor: "#0958d9",
};

const footerStyle: React.CSSProperties = {
    textAlign: "center",
    color: "#fff",
    backgroundColor: "#4096ff",
};

const layoutStyle = {
    overflow: "hidden",
    height: "100vh",
    width: "100vw",
};

export default function PageLayout() {
    return (
        <Flex gap="middle" wrap="wrap">
            <Layout style={layoutStyle}>
                <Header style={headerStyle}>
                    <HeaderBar />
                    <MenuBar />
                    <SubMenuBar />
                </Header>
                <Content style={contentStyle}>
                    <Outlet />
                </Content>
                <Footer style={footerStyle}>Footer</Footer>
            </Layout>
        </Flex>
    );
}
