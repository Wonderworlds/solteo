import React from 'react';

interface FilterProps {
  name: string;
  isClicked: number;
  self: number;
  setIsClicked: React.Dispatch<React.SetStateAction<number>>;
}

const Filter: React.FC<FilterProps> = ({ isClicked, setIsClicked, name, self }) => {
  return (
    <>
      {isClicked === self ? (
        <div className="filterIsClicked" onClick={() => setIsClicked(self)}>
          {name}
        </div>
      ) : (
        <div className="filterIsNotClicked" onClick={() => setIsClicked(self)}>
          {name}
        </div>
      )}
    </>
  );
};

export default Filter;
