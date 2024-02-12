import { Inter, Lexend } from 'next/font/google'
import clsx from 'clsx'

import '@/styles/tailwind.css'

export const metadata = {
  title: {
    template: '%s - GAN Conferencing',
    default: 'GAN Conferencing - The best operator assisted services in the business!',
  },
  description:
    'The best human operators combined with state of the art technology to deliver the best operator assisted services in the business! If you ever have had issues with your current provider, give us a try. We will not disappoint you! There is a reason why we have been in business for over 20 years.',
}

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

const lexend = Lexend({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-lexend',
})

export default function RootLayout({ children }) {
  return (
    <html
      lang="en"
      className={clsx(
        'h-full scroll-smooth bg-white antialiased',
        inter.variable,
        lexend.variable,
      )}
    >
      <body className="flex h-full flex-col">{children}</body>
    </html>
  )
}
