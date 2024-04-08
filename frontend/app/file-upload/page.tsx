"use client";
import React, { useState } from "react";
import { Button } from '@/components/ui/button';
import { FaCloudUploadAlt } from "react-icons/fa";

const FileUploadPage: React.FC = () => {
  const [filesA, setFilesA] = useState<File[]>([]);
  const [filesB, setFilesB] = useState<File[]>([]);

  const handleFileChange = (party: string) => (event: React.ChangeEvent<HTMLInputElement>) => {
    const newFiles = event.target.files;
    if (newFiles) {
      if (party == "party-a")
        setFilesA([...filesA, ...Array.from(newFiles)]);
      else
        setFilesB([...filesB, ...Array.from(newFiles)]);
    }
  };

  const handleFileChangePartyA = handleFileChange('party-a');
  const handleFileChangePartyB = handleFileChange('party-b');

  const handleSubmit = async () => {
    let formData = new FormData();
    filesA.forEach((file, index) => {
      formData.append(`partyA-${index}`, file);
    });
    filesB.forEach((file, index) => {
      formData.append(`partyB-${index}`, file);
    });

    const response = await fetch('/submit', {
      method: 'POST',
      body: formData
    });

    if (response.ok) {
      console.log('Files submitted successfully');
    } else {
      console.error('Failed to submit files');
    }
  }

  return (
    <main className="p-4"> 
      <p className="text-2xl text-center">Upload documents for each of the parties</p>
      <div className="flex p-4 justify-center">
        <div className="w-1/2 p-4 m-2 flex flex-col items-center border shadow-lg">
          <span className="text-xl">Party A</span>
          <FaCloudUploadAlt size={140} />
          <input type="file" onChange={handleFileChangePartyA} multiple />
        </div>
        <div className="w-1/2 p-4 m-2 flex flex-col items-center border shadow-lg">
          <span className="text-xl">Party B</span>
          <FaCloudUploadAlt size={140} />
          <input type="file" onChange={handleFileChangePartyB} multiple />
        </div>
      </div>
      <div className="flex justify-center">
        <Button size="lg" onClick={handleSubmit}>Submit</Button>
      </div>
    </main>
  );
};

export default FileUploadPage;