
import { CharacterTextSplitter } from "langchain/text_splitter";


const splitter = new CharacterTextSplitter({
  separator: " ",
  chunkSize: 7,
  chunkOverlap: 3,
});
const output = await splitter.createDocuments([text]);
