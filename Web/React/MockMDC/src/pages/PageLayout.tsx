import { Layout, Flex } from "antd";
import HeaderBar from "../components/header/HeaderBar";
import MenuBar from "../components/header/MenuBar";
import SubMenuBar from "../components/header/SubMenuBar";
import { Outlet, redirect } from "react-router-dom";

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

const contentStyle = {
    overflow: "hidden",
    height: "100%",
    width: "100%",
    padding: 10,
};

export default function PageLayout() {
    return (
        <Layout style={layoutStyle}>
            <Header style={headerStyle}>
                <HeaderBar />
                <MenuBar />
                <SubMenuBar />
            </Header>
            <Layout>
                <Content style={contentStyle}>
                    <Outlet />
                </Content>
            </Layout>
            <Footer style={footerStyle}>Footer</Footer>
        </Layout>
    );
}
