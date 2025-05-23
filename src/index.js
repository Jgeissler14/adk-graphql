const { ApolloServer, gql } = require('apollo-server');
const { getSampleData } = require('./googleAdk');

const typeDefs = gql`
  type Query {
    adkData: String
  }
`;

const resolvers = {
  Query: {
    adkData: async () => {
      return await getSampleData();
    }
  }
};

async function startServer() {
  const server = new ApolloServer({ typeDefs, resolvers });
  const { url } = await server.listen();
  console.log(`Server ready at ${url}`);
}

startServer();
