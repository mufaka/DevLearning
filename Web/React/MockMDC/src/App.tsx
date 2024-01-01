// import { useState } from "react";
import "./App.css";
import { Layout, Flex } from "antd";

const { Header, Footer, Content } = Layout;

// TODO: These styles need to go in App.css or use tailwind
const headerStyle: React.CSSProperties = {
    textAlign: "center",
    color: "#fff",
    height: 64,
    paddingInline: 48,
    lineHeight: "64px",
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
                <Header style={headerStyle}>Header</Header>
                <Content style={contentStyle}>Content</Content>
                <Footer style={footerStyle}>Footer</Footer>
            </Layout>
        </Flex>
    );
}

export default App;
