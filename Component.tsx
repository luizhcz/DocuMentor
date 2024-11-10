import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Checkbox } from "@/components/ui/checkbox"
import { User, Mail, Briefcase, GraduationCap, BookOpen, Sparkles, Brain } from 'lucide-react'

export default function Component() {
  const [interests, setInterests] = useState<string[]>([])
  const [currentStep, setCurrentStep] = useState(0)
  const [isLoading, setIsLoading] = useState(false)

  const handleInterestChange = (interest: string) => {
    setInterests(prev =>
      prev.includes(interest)
        ? prev.filter(i => i !== interest)
        : [...prev, interest]
    )
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    // Simulate form submission
    await new Promise(resolve => setTimeout(resolve, 2000))
    setIsLoading(false)
    // Here you would add the actual form submission logic
  }

  const formSteps = [
    { title: "Personal Information", icon: User },
    { title: "Education and Profession", icon: GraduationCap },
    { title: "Interests", icon: BookOpen },
  ]

  useEffect(() => {
    const interval = setInterval(() => {
      const neurons = document.querySelectorAll('.neuron')
      neurons.forEach((neuron) => {
        neuron.classList.add('pulse')
        setTimeout(() => neuron.classList.remove('pulse'), 1000)
      })
    }, 2000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-600 p-4 overflow-hidden">
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute inset-0 bg-black opacity-50"></div>
        {[...Array(20)].map((_, i) => (
          <div
            key={i}
            className="neuron absolute w-2 h-2 bg-white rounded-full"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animation: `float ${5 + Math.random() * 10}s infinite`,
            }}
          ></div>
        ))}
      </div>
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
        className="w-full max-w-2xl relative"
      >
        <Card className="backdrop-blur-2xl bg-white/10 border border-white/20 shadow-2xl overflow-hidden">
          <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400"></div>
          <CardHeader className="space-y-1 relative z-10">
            <motion.div
              initial={{ y: -20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.2 }}
            >
              <CardTitle className="text-4xl font-bold text-center bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-pink-400 pb-2 flex items-center justify-center">
                <Brain className="w-8 h-8 mr-2 inline-block" />
                DocuMentor
              </CardTitle>
            </motion.div>
            <CardDescription className="text-center text-lg text-white/90">
              Embark on a personalized and innovative learning journey
            </CardDescription>
          </CardHeader>
          <form onSubmit={handleSubmit}>
            <CardContent className="grid gap-6 relative z-10">
              <div className="flex justify-between mb-4">
                {formSteps.map((step, index) => (
                  <motion.div
                    key={index}
                    className={`flex flex-col items-center ${
                      currentStep >= index ? 'text-white' : 'text-white/50'
                    }`}
                    initial={{ y: 20, opacity: 0 }}
                    animate={{ y: 0, opacity: 1 }}
                    transition={{ delay: 0.1 * index }}
                  >
                    <step.icon className="w-6 h-6 mb-1" />
                    <span className="text-xs">{step.title}</span>
                  </motion.div>
                ))}
              </div>
              <AnimatePresence mode="wait">
                {currentStep === 0 && (
                  <motion.div
                    key="step1"
                    initial={{ x: 20, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    exit={{ x: -20, opacity: 0 }}
                    transition={{ duration: 0.3 }}
                    className="space-y-4"
                  >
                    <div className="grid grid-cols-2 gap-4">
                      <div className="space-y-2">
                        <Label htmlFor="name" className="text-white/90">Name</Label>
                        <Input id="name" placeholder="Your full name" className="bg-white/10 border-white/30 focus:border-white focus:bg-white/30 transition-all duration-300 placeholder-white/50 text-white" />
                      </div>
                      <div className="space-y-2">
                        <Label htmlFor="age" className="text-white/90">Age</Label>
                        <Input id="age" placeholder="Your age" type="number" className="bg-white/10 border-white/30 focus:border-white focus:bg-white/30 transition-all duration-300 placeholder-white/50 text-white" />
                      </div>
                    </div>
                    <div className="space-y-2">
                      <Label htmlFor="email" className="text-white/90">Email</Label>
                      <Input id="email" placeholder="your.email@example.com" type="email" className="bg-white/10 border-white/30 focus:border-white focus:bg-white/30 transition-all duration-300 placeholder-white/50 text-white" />
                    </div>
                  </motion.div>
                )}
                {currentStep === 1 && (
                  <motion.div
                    key="step2"
                    initial={{ x: 20, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    exit={{ x: -20, opacity: 0 }}
                    transition={{ duration: 0.3 }}
                    className="space-y-4"
                  >
                    <div className="space-y-2">
                      <Label htmlFor="profession" className="text-white/90">Profession</Label>
                      <Input id="profession" placeholder="Your current profession" className="bg-white/10 border-white/30 focus:border-white focus:bg-white/30 transition-all duration-300 placeholder-white/50 text-white" />
                    </div>
                    <div className="space-y-2">
                      <Label htmlFor="education" className="text-white/90">Education Level</Label>
                      <Select>
                        <SelectTrigger style={{color: "rgba(255, 255, 255, 0.2)"}} id="education" className="bg-white/10 placeholder:text-white/20 border-white/30 focus:border-white focus:bg-white/30 transition-all duration-300 text-white">
                          <SelectValue placeholder="Select your education level" />
                        </SelectTrigger>
                        <SelectContent className="bg-white/90 backdrop-blur-lg">
                          <SelectItem value="elementary">Elementary School</SelectItem>
                          <SelectItem value="highschool">High School</SelectItem>
                          <SelectItem value="bachelor">Bachelor's Degree</SelectItem>
                          <SelectItem value="postgrad">Postgraduate</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>
                  </motion.div>
                )}
                {currentStep === 2 && (
                  <motion.div
                    key="step3"
                    initial={{ x: 20, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    exit={{ x: -20, opacity: 0 }}
                    transition={{ duration: 0.3 }}
                    className="space-y-4"
                  >
                    <Label className="text-white/90">Interests (select all that apply)</Label>
                    <div className="grid grid-cols-2 gap-4">
                      {['Technology', 'Science', 'Arts', 'History', 'Mathematics', 'Languages', 'Business', 'Health'].map((interest) => (
                        <motion.div
                          key={interest}
                          className="flex items-center space-x-2 bg-white/10 p-3 rounded-lg transition-all duration-300 hover:bg-white/20"
                          whileHover={{ scale: 1.05 }}
                          whileTap={{ scale: 0.95 }}
                        >
                          <Checkbox
                            id={interest}
                            checked={interests.includes(interest)}
                            onCheckedChange={() => handleInterestChange(interest)}
                            className="border-white/50 text-pink-500 focus:ring-pink-500"
                          />
                          <label
                            htmlFor={interest}
                            className="text-sm font-medium leading-none text-white/90 cursor-pointer select-none"
                          >
                            {interest}
                          </label>
                        </motion.div>
                      ))}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </CardContent>
            <CardFooter className="flex justify-between">
              {currentStep > 0 && (
                <Button
                  type="button"
                  variant="outline"
                  onClick={() => setCurrentStep(step => step - 1)}
                  className="bg-white/10 border-white/30 text-white hover:bg-white/20"
                >
                  Back
                </Button>
              )}
              {currentStep < formSteps.length - 1 ? (
                <Button
                  type="button"
                  onClick={() => setCurrentStep(step => step + 1)}
                  className="ml-auto bg-gradient-to-r from-blue-500 to-pink-500 hover:from-blue-600 hover:to-pink-600 text-white"
                >
                  Next
                </Button>
              ) : (
                <Button
                  type="submit"
                  className="ml-auto bg-gradient-to-r from-blue-500 to-pink-500 hover:from-blue-600 hover:to-pink-600 text-white"
                  disabled={isLoading}
                >
                  {isLoading ? (
                    <motion.div
                      className="flex items-center"
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                    >
                      <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      Processing...
                    </motion.div>
                  ) : (
                    <>
                      <Sparkles className="w-5 h-5 mr-2" />
                      Start My Journey
                    </>
                  )}
                </Button>
              )}
            </CardFooter>
          </form>
        </Card>
      </motion.div>
      <style jsx global>{`
        @keyframes float {
          0%, 100% { transform: translateY(0); }
          50% { transform: translateY(-10px); }
        }
        .neuron {
          transition: all 0.5s ease;
        }
        .neuron.pulse {
          transform: scale(2);
          opacity: 0;
        }
      `}</style>
    </div>
  )
}