import { AppScreen } from '../../../ui'
import { OutlinedField } from '../components/OutlinedField'
import { PhoneStatusBar } from '../components/PhoneStatusBar'
import { SignupActions } from '../components/SignupActions'
import { SignupHeader } from '../components/SignupHeader'
import { SignupTitle } from '../components/SignupTitle'
import { filledForm, signup, socialProviders } from '../data'
import { theme } from '../theme'

/** Sign-up form; `filled` shows the entered credentials and the strength hint (pushing actions down). */
export function SignUpScreen({ filled = false }: { filled?: boolean }) {
  return (
    <AppScreen className="font-figtree">
      <PhoneStatusBar />
      <SignupHeader skip={signup.skip} />
      <SignupTitle lines={signup.title} top={222} />
      <OutlinedField top={308} placeholder={signup.emailPlaceholder} value={filled ? filledForm.email : undefined} />
      <OutlinedField
        top={372}
        placeholder={signup.passwordPlaceholder}
        maskLength={filled ? filledForm.passwordLength : undefined}
        revealable
      />
      {filled && (
        <div className="absolute text-[12.5px]" style={{ left: 20, top: 437 }}>
          <span className="text-[#77777d]">{filledForm.strengthLabel} </span>
          <span className="font-semibold" style={{ color: theme.green }}>
            {filledForm.strength}
          </span>
        </div>
      )}
      <SignupActions
        top={filled ? 471 : 435}
        cta={signup.cta}
        or={signup.or}
        providers={socialProviders}
        haveAccount={signup.haveAccount}
        signIn={signup.signIn}
        refer={signup.refer}
        highlightedKey={filled ? 'apple' : undefined}
      />
    </AppScreen>
  )
}
