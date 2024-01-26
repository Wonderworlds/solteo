export interface RecordProps {
  year: string;
  date: string;
  type_production: string;
  type_injection: string;
  mw: number;
}

const Record = (props: RecordProps) => {
  return (
    <li className="record">
      <div className="recordLeft">
        <p>
          {props.type_production} | {props.type_injection}
        </p>
      </div>
      <div className="recordMiddle">
        <div>{props.mw} MW</div>
      </div>
      <div className="recordRight">
        <div className="recordRightTop">{props.year}</div>
        <div className="recordRightBot">{props.date}</div>
      </div>
    </li>
  );
};

export default Record;
