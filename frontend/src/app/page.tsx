import prisma from "@/lib/database";

const Page = async () => {
  let testRows = [];

  try {
    testRows = await prisma.testTable.findMany();
    console.log("Fetched rows:", testRows);
  } catch (error) {
    console.error("Prisma query failed:", error);
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1>Test Table Data</h1>
      <ul>
        {testRows.map((row) => (
          <li key={row.id}>
            {row.id}: {row.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Page;
