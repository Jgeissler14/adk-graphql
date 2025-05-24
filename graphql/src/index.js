const { ApolloServer, gql } = require('apollo-server');

const typeDefs = gql`
  type Query {
    customer: String
    salesRecord: String
    product: String
  }
`;

const resolvers = {
  Query: {
    customer: async () => {
      return "John Doe";
    },
    salesRecord: async () => {
      return "Sales Record 12345";
    },
    product: async () => {
      return "Product XYZ";
    },
  }
};

async function startServer() {
  const server = new ApolloServer({ typeDefs, resolvers });
  const { url } = await server.listen();
  console.log(`Server ready at ${url}`);
}

startServer();
