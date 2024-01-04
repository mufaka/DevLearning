import { Card, Col, Row } from "antd";
import HomeCalendar from "../components/home/HomeCalendar";

export default function Home() {
    const gridSpacing = 8;

    return (
        <Row gutter={gridSpacing} style={{ height: "100%" }}>
            <Col span={6} className="flex flex-col gap-2">
                <Row gutter={gridSpacing} className="flex-initial">
                    <Col span={8}>Worksheet</Col>
                    <Col span={8}>Charge Slip</Col>
                    <Col span={8}>Message</Col>
                </Row>
                <Row
                    gutter={gridSpacing}
                    className="flex-initial"
                    style={{ flex: "0 1 auto" }}
                >
                    <Col span={24}>
                        <Card size="small">
                            <HomeCalendar />
                        </Card>
                    </Col>
                </Row>
                <Row gutter={gridSpacing} className="flex-auto">
                    <Col span={24}>
                        <Card
                            size="small"
                            title="Patient Tracking"
                            style={{ height: "100%" }}
                        ></Card>
                    </Col>
                </Row>
            </Col>
            <Col span={12} className="flex flex-col gap-2">
                <Row gutter={gridSpacing} className="flex-initial">
                    <Col>Office Provider Drop Downs</Col>
                </Row>
                <Row gutter={gridSpacing} className="flex-auto">
                    <Col span={24}>
                        <Card
                            size="small"
                            title="Today's Appointments"
                            style={{ height: "100%" }}
                        ></Card>
                    </Col>
                </Row>
                <Row gutter={gridSpacing} className="flex-initial">
                    <Col span={12} style={{ height: "220px" }}>
                        <Card
                            size="small"
                            title="Current Appointments"
                            style={{ height: "100%" }}
                        ></Card>
                    </Col>
                    <Col span={12}>
                        <Card
                            size="small"
                            title="Events / Holidays"
                            style={{ height: "100%" }}
                        ></Card>
                    </Col>
                </Row>
            </Col>
            <Col span={6} className="flex flex-col gap-2">
                <Row gutter={gridSpacing} className="flex-auto">
                    <Col span={24}>
                        <Card
                            size="small"
                            title="Your Reminders"
                            style={{ height: "100%" }}
                        ></Card>
                    </Col>
                </Row>
            </Col>
        </Row>
    );
}
