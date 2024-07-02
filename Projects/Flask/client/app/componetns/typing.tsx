import React, { useState, useEffect } from 'react';

export const TypingEffect = ({
  text,
  speed = 50,
}: {
  text: string;
  speed: number;
}) => {
  const [displayedText, setDisplayedText] = useState('');

  useEffect(() => {
    let index = 0;
    const interval = setInterval(() => {
      if (index < text.length) {
        setDisplayedText((prev) => prev + text[index]);
        index++;
      } else {
        clearInterval(interval);
      }
    }, speed);

    // Cleanup the interval on component unmount
    return () => clearInterval(interval);
  }, [text, speed]);

  // Function to convert '\n' to <br> tags
  const formatTextWithBreaks = (text: string): any => {
    return text.split('\n').map((line, index) => {
      return (
        <React.Fragment key={index}>
          {line}
          <br />
        </React.Fragment>
      );
    });
  };

  return <pre>{formatTextWithBreaks(displayedText)}</pre>;
};
