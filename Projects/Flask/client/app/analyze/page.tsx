'use client';

import axios from 'axios';
import React, { useState } from 'react';

function Code() {
  const [data, setData] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchResponse = (codeSnippet: any) => {
    setLoading(true);
    axios({
      method: 'post',
      url: 'http://127.0.0.1:5000/code-analyzer',
      data: {
        query: codeSnippet,
      },
    })
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('There was an error!', error);
      });
  };

  const handleClick = () => {
    var code = document.getElementById('code-source')?.value;
    fetchResponse(code);
  };

  return (
    <div id="main-container" className="dark h-full max-h-max">
      <div className="flex h-full ">
        <div className="p-10">
          {loading && 'Fetching the information, Please wait ....'}
          <pre className="p-1 mb-96 pb-60 block float-left w-full">{data}</pre>
        </div>

        <footer className="max-w-4xl mx-auto sticky bottom-0 z-10 p-3 sm:py-6">
          <div className="fixed right-0 bottom-0 w-full  ">
            <textarea
              id="code-source"
              className="p-4 pb-12 h-40 block w-full bg-gray-100 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500"
              placeholder="paste the code here .... "
            ></textarea>

            <div className="absolute bottom-px inset-x-px p-2 rounded-b-lg bg-gray-100 dark:bg-neutral-800">
              <div className="flex justify-between items-center ">
                <div className="flex items-center"></div>

                <div className="flex items-center gap-x-1 ">
                  <button
                    type="button"
                    className="inline-flex flex-shrink-0 justify-center items-center size-8 rounded-lg text-white bg-blue-600 hover:bg-blue-500 focus:z-10 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    onClick={() => handleClick()}
                  >
                    <svg
                      className="flex-shrink-0 size-3.5"
                      xmlns="http://www.w3.org/2000/svg"
                      width="16"
                      height="16"
                      fill="currentColor"
                      viewBox="0 0 16 16"
                    >
                      <path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083l6-15Zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471-.47 1.178Z" />
                    </svg>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </footer>
      </div>
    </div>
  );
}

export default Code;
