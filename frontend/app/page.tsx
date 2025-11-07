export default async function Home() {
  // Em produção de frontend (rodando no navegador), use a URL pública:
  const apiUrl = process.env.INTERNAL_API_URL || 'http://backend:5000';
  const res = await fetch(`${apiUrl}`, { cache: 'no-store' });
  const text = await res.text();

  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h1>Next.js + Flask + MySQL (Docker)</h1>
      <p>Backend disse: <strong>{text}</strong></p>
      <p><strong>Micha e Dudu</strong></p>
    </main>
  );
}
