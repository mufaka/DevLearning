// import { useState } from "react";
import "./App.css";
import { Layout, Flex } from "antd";
import HeaderBar from "./components/header/HeaderBar";
import MenuBar from "./components/header/MenuBar";
import SubMenuBar from "./components/header/SubMenuBar";

const { Header, Footer, Content } = Layout;

// TODO: These styles need to go in App.css?
const headerStyle: React.CSSProperties = {
    textAlign: "center",
    color: "#fff",
    height: 104,
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

function App() {
    // const [count, setCount] = useState(0);

    return (
        <Flex gap="middle" wrap="wrap">
            <Layout style={layoutStyle}>
                <Header style={headerStyle}>
                    <HeaderBar />
                    <MenuBar />
                    <SubMenuBar />
                </Header>
                <Content style={contentStyle}>Content</Content>
                <Footer style={footerStyle}>Footer</Footer>
            </Layout>
        </Flex>
    );
}

export default App;
