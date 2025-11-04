"use client";

export default function ClearCacheButton() {
  const handleClick = async () => {
    await fetch("/api/cache", { method: "DELETE" });
    alert("Cache cleared");
  };

  return (
    <button
      onClick={handleClick}
      className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
    >
      Clear Cache
    </button>
  );
}
