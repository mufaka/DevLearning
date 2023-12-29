import styles from "./todoitem.module.css";

interface Props {
    item: string;
}

export default function TodoItem({ item }: Props) {
    return (
        <div className={styles.itemContainer}>
            <div className={styles.item}>{item}</div>
            <hr className={styles.line} />
        </div>
    );
}
