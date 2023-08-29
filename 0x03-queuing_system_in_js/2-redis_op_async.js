import redis from "redis";
import util from 'util';
const client = redis.createClient();

client
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

let displaySchoolValue = async schoolName => {
    const getAsync = util.promisify(client.get).bind(client);
    console.log(await getAsync(schoolName));
};
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
