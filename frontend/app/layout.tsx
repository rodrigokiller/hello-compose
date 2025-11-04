// frontend/app/layout.tsx
export const metadata = {
  title: 'Hello Compose',
  description: 'Next.js + Flask + MySQL',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
