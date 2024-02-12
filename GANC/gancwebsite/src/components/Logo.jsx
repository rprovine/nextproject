
import Image from 'next/image';
import logo from '/src/images/logos/logo-light.png';

export function Logo(props) {
  return (
    <div {...props}>
      <Image src={logo} alt="Logo" />
    </div>
  );
}